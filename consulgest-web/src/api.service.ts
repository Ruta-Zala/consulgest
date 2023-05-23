import axios from 'axios';

export const apiService = axios.create({
	baseURL: import.meta.env.VITE_API_URL,
});

apiService.interceptors.request.use(
	(config) => {
		const token = localStorage.getItem('access_token');
		if (token) {
			config.headers.Authorization = `Bearer ${token}`;
		}
		return config;
	},
	(error) => Promise.reject(error),
);

apiService.interceptors.response.use(
	(response) => response,
	(error) => {
		if (error.response.status === 401) {
			localStorage.removeItem('access_token');
			localStorage.removeItem('currentUser');
			window.location.href = '/';
		}
		return Promise.reject(error);
	},
);
