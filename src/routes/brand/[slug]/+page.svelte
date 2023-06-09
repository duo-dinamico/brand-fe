<script lang="ts">
	import { onMount } from 'svelte';
	import { page } from '$app/stores';

	let brand:any = [];

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
				{#if key != "category"}
				{key} - {value}
				{:else}
				<a href="/categories/{value.id}">{key} - {value.id}</a>
				{/if}
			</li>
		{/each}
	</ul>
</div>
