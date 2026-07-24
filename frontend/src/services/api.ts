import axios from 'axios';

// Creamos una instancia de axios configurada para apuntar a tu backend local
export const api = axios.create({
  baseURL: 'http://localhost:8000',
});