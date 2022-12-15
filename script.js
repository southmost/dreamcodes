// Define the encode function
// Define the encode function
function encode(width, height, steps, sampler, model, cfg_scale, number_of_images, clip_guidance) {
  // Create an encoded values object
  const encoded_values = {};

  // Encode the variable names and values using the cypher dictionaries
  for (const [variable, value] of Object.entries({ width, height, steps, sampler, model, cfg_scale, number_of_images, clip_guidance })) {
    if (value === undefined) {
      continue;
    }
    const encoded_name = cypher[variable];
    const encoded_value = value_cypher[value];
    encoded_values[encoded_name] = encoded_value;
  }

  // Return the encoded values
  return encoded_values;
}

  // Define the decode function
function decode(encoded_values) {
  // Create a decoded values object
  const decoded_values = {};

  // Decode the short code using the cypher dictionaries
  for (const [encoded_name, encoded_value] of Object.entries(encoded_values)) {
    if (encoded_name in cypher) {
      const variable = Object.keys(cypher).find(key => cypher[key] === encoded_name);
      const value = Object.keys(value_cypher).find(key => value_cypher[key] === encoded_value);
      decoded_values[variable] = value;
    }
  }

  // Return the decoded values
  return decoded_values;
}

// Add event listeners to the forms
encodeForm.addEventListener('submit', (event) => {
  // Prevent the default form submission behavior
  event.preventDefault();

  // Get the input values
  const width = encodeForm.elements.width.value;
  const height = encodeForm.elements.height.value;
  const steps = encodeForm.elements.steps.value;
  const sampler = encodeForm.elements.sampler.value;
  const model = encodeForm.elements.model.value;
  const cfg_scale = encodeForm.elements.cfg_scale.value;
  const number_of_images = encodeForm.elements.number_of_images.value;
  const clip_guidance = encodeForm.elements.clip_guidance.value;
});

