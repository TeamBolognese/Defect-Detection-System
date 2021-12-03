
<!-- [ SCRIPT ] -->
<script>

    // [ IMPORTS: extensions ]
    import { createPDF, openPDF } from '$lib/pdf-lib.js';
    import { renderCanvas } from '$lib/renderCanvas.js';

    // [ IMPORTS: system ]
    import { fade } from 'svelte/transition'
    import { onMount } from 'svelte';

    // [ IMPORTS: components ]
    import Analytics from '../components/Analytics.svelte';
    import ProcessSchedule from '../components/ProcessSchedule.svelte';


    // [ PROPS ]
    let acceptance_complete = false;
    const analytics = {
        defects:     true,       // has defects / no defects
        defect_rate: 0.15,       // percentage
        invoice:     1200000,    // price of no-defect cargo
    }


    // [ HOOKS ]
    onMount(() => {
        renderCanvas();
    });

</script>


<!-- [ TEMPLATE: Monitoring ] -->
<svelte:head>
    <title>Monitoring</title>
</svelte:head>

<main in:fade='{{ duration: 100 }}' out:fade|local='{{ duration: 100 }}' class = 'monitoring'>

    <!-- [ section: zone tabs ] -->
    <ul class = 'zone-tabs'>
        <li class="tab active"><a href = '/'>Зона А</a></li>
        <li class="tab"><a href = 'zoneB'>Зона Б</a></li>
        <li class="tab">Зона В</li>
    </ul>

    <!-- [ section: dashboard ] -->
    <div class="dashboard">

        <!-- process info -->
        <p class = 'process-info'>
            <span class = 'supplier'>ООО Белкин и Стрелкин</span>
            Приемка: гречка, 15 тонн
        </p>

        <!-- video canvas & analytics -->
        <div class="monitor">
            <div class="video">
                <video src="/img/stream_example.mov" loop = 'true' muted = 'true' autoplay="autoplay"></video>
            </div>
            <Analytics { analytics } />
        </div>

        <!-- button: complete acceptance -->
        {#if !acceptance_complete}
            <button on:click|preventDefault={ () => { acceptance_complete = true ; createPDF() } } class="CTA complete-acceptance">завершить приемку</button>
        {:else}
            <div class="hidden-area">
                <a href = '' on:click={ openPDF } class="CTA bg-orange make-invoice view-pdf">выставить счет</a>
                <a href = 'suppliers-overview' class="CTA order">дозаказать</a>
            </div>
        {/if}

    </div>

    <!-- [ section: process schedule ] -->
    <ProcessSchedule />

</main>
