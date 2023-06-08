<script lang="ts">
	import { onMount } from 'svelte';
	import { page } from '$app/stores';

	let brand = [];

	onMount(() => {
		fetch(`https://brands.duodinamico.online/brands/${$page.params.slug}`)
			.then((response) => response.json())
			.then((result) => (brand = Object.entries(result.brands[0])));
	});
</script>

<div class="absolute top-16">
	<h1 class="text-xl font-semibold">Brand</h1>
	<ul>
		{#each brand as [key, value]}
			<li>
				{key} - {value}
			</li>
		{/each}
	</ul>
</div>
