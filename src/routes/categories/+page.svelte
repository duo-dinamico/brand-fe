<script lang="ts">
	import type { PageData } from './$types';

	export let data: PageData;

	const { categories } = data;
</script>

{#if categories.length}
	<div class="overflow-x-auto">
		<table class="table table-zebra">
			<thead>
				<tr>
					<th>Category Name</th>
				</tr>
			</thead>
			<tbody>
				{#each categories as category (category.id)}
					<tr>
						<th
							><a class="link link-primary" href="/categories/{category.id}">{category.name}</a></th
						>
					</tr>
				{/each}
			</tbody>
		</table>
	</div>
{:else}<span class="loading loading-spinner loading-lg" />{/if}
