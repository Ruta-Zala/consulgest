import { useLocalStorage } from '@vueuse/core';

interface User {
	pk: number;
	username: string;
	email: string;
	first_name: string;
	last_name: string;
}

export function useCurrentUser() {
	return useLocalStorage<User | null>('currentUser', null, {
		serializer: {
			read: (data: any) => (data ? JSON.parse(data) : null),
			write: (data: any) => JSON.stringify(data),
		},
	});
}
