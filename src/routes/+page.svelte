<script lang="ts">
	import type { PageData } from './$types';

	export let data: PageData;

	const { brands } = data;
</script>

<!--    
   // interface CategoryBase {
    //   id: string;
    //   name: string;
    // }
  
    // interface UserBase {
    //   id: string;
    //   username: string;
    // }
  
    // interface Brand {
    //   id: string;
    //   name: string;
    //   category: CategoryBase;
    //   description: string;
    //   average_price: number;
    //   line_address_1: string;
    //   line_address_2: string;
    //   city: string;
    //   postal_code: string;
    //   created_at: string;
    //   created_by: UserBase;
    //   updated_at: string;
    //   updated_by: UserBase;
    //   deleted_at: string;
    //   deleted_by: UserBase;
    // } -->

{#if brands.length}
	<div class="overflow-x-auto">
		<table class="table table-zebra">
			<thead>
				<tr>
					<th>Brand Name</th>
					<th>Description</th>
				</tr>
			</thead>
			<tbody>
				{#each brands as brand (brand.id)}
					<tr>
						<th><a class="link link-primary" href="/brand/{brand.id}">{brand.name}</a></th>
						<th>{brand.description}</th>
					</tr>
				{/each}
			</tbody>
		</table>
	</div>
{:else}<span class="loading loading-spinner loading-lg" />{/if}
