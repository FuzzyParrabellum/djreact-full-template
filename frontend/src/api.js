import axios from "axios";
import { ACCESS_TOKEN } from "./constants";

// api base url, localy VITE_API_URL="http://localhost:8000"
const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
});

// verify if user is authenticated with right token
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem(ACCESS_TOKEN);
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// instead of default axios, we will use this variable everywhere in the rest
// of the code
export default api;
