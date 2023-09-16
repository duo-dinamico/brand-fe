import { error } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async () => {
	const brands = await fetch('https://brands.duodinamico.online/brands/')
		.then((response) => response.json())
		.then((result) => result);

	if (brands) {
		return brands;
	}

	throw error(404, 'Not found');
};
