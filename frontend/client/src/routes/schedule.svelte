
<!-- [ SCRIPT ] -->
<script>

    // [ IMPORTS: components ]
    import { fade } from 'svelte/transition'

</script>


<!-- [ TEMPLATE: Schedule ] -->
<svelte:head>
    <title>Schedule</title>
</svelte:head>

<main in:fade='{{ duration: 100 }}' out:fade|local='{{ duration: 100 }}' class = 'schedule'>
    <h1>Schedule page</h1>
</main>
