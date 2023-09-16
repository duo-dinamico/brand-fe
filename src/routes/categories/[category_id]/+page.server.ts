import { error } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ params }) => {
	const category = await fetch(`https://brands.duodinamico.online/categories/${params.category_id}`)
		.then((response) => response.json())
		.then((result) => result.categories[0]);

	if (category) {
		return category;
	}

	throw error(404, 'Not found');
};
