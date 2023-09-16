import { error } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async () => {
	const categories = await fetch('https://brands.duodinamico.online/categories/')
		.then((response) => response.json())
		.then((result) => result);

	if (categories) {
		return categories;
	}

	throw error(404, 'Not found');
};
