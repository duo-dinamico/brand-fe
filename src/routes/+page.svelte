<script lang="ts">
  import { onMount } from "svelte";

  let brands = [];

  onMount(() => {
    fetch("https://brands.duodinamico.online/brands/")
      .then((response) => response.json())
      .then((result) => (brands = result.brands));
  });
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

<body class="absolute inset-x-0 top-16">
  <h1 class="text-xl font-semibold">Brand List</h1>
  <ul>
    {#each brands as brand (brand.id)}
      <li>{brand.name} - link</li>
    {:else}
      <h2>wait</h2>
    {/each}
  </ul>
</body>
