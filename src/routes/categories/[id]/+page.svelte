<script lang="ts">
	import { onMount } from 'svelte';
	import { page } from '$app/stores';

	let category:any = [];

	onMount(() => {
		fetch(`https://brands.duodinamico.online/categories/${$page.params.id}`)
			.then((response) => response.json())
			.then((result) => (category = Object.entries(result.categories[0])));
	});
</script>

<div class="absolute top-16">
	<h1 class="text-xl font-semibold">Category</h1>
	<ul>
		{#each category as [key, value]}
			<li>
				{key} - {value}
			</li>
		{/each}
	</ul>
</div>
