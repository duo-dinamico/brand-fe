import type { Actions } from './$types';
import { redirect } from '@sveltejs/kit';

export const actions = {
	login: async ({ request, cookies }) => {
		const data = await request.formData();

		const response = await fetch('https://brands.duodinamico.online/login', {
			method: 'POST',
			body: data
		}).then((data) => data.json());

		if (response) {
			// isAuthenticated = true;

			cookies.set('session', JSON.stringify(response), {
				path: '/',
				httpOnly: true,
				maxAge: 60 * 60 * 24 * 30
			});
			console.log(JSON.parse(cookies.get('session')));
			throw redirect(303, '/');
		}
	}
} satisfies Actions;
