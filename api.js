const API_URL = 'http://localhost:5005';

export async function predictImage(file, language = 'en') {
  const formData = new FormData();
  formData.append('image', file);

  console.log(`Making API request with language: ${language}`);
  console.log(`Full URL: ${API_URL}/predict?lang=${language}`);

  const response = await fetch(`${API_URL}/predict?lang=${language}`, {
    method: 'POST',
    body: formData,
  });

  if (!response.ok) {
    throw new Error('Prediction failed');
  }

  const data = await response.json();
  console.log('API Response:', data);
  return data;
}
