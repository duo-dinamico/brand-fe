import type { Actions } from './$types';

export const actions = {
	login: async ({ request }) => {
		const data = await request.formData();

		const response = await fetch('https://brands.duodinamico.online/login', {
			method: 'POST',
			body: data
		});
		console.log(await response.json());
	}
} satisfies Actions;
