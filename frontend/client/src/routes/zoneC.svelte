
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
    let analytics_received  = false;
    let acceptance_complete = false;
    const analytics = {
        defects:     false,      // has defects / no defects
        defect_rate: 0,          // percentage
        invoice:     2100205,    // price of no-defect cargo
    }

    onMount(() => {
        renderCanvas();

        // get > image analytics from URI
        const urlParams = new URLSearchParams(window.location.search);
        let state = urlParams.get('state');

        if( state !== null ) {
            analytics_received = true
        }
    });


</script>


<!-- [ TEMPLATE: Monitoring ] -->
<svelte:head>
    <title>Monitoring</title>
</svelte:head>

<!-- modal: image analytics -->
{#if analytics_received}
    <div class="modal-result">
        <div class="overlay" on:click={ () => { analytics_received = false } }></div>
        <div class="message">
            <h5 class="title">Результаты анализа:</h5>
            <div class="content">
                <p><img src="https://final.teambolognese.ru/res.png" alt="defect highlighted"></p>
            </div>
        </div>
    </div>
{/if}

<main in:fade='{{ duration: 100 }}' out:fade|local='{{ duration: 100 }}' class = 'monitoring'>

    <!-- [ section: zone tabs ] -->
    <ul class = 'zone-tabs'>
        <li class="tab"><a href = '/'>Зона А</a></li>
        <li class="tab"><a href = 'zoneB'>Зона Б</a></li>
        <li class="tab active">Зона В</li>
    </ul>

    <!-- [ section: dashboard ] -->
    <div class="dashboard">

        <!-- process info -->
        <p class = 'process-info'>
            <span class = 'supplier'>ООО Трио</span>
            Приемка: овес, 20 тонн
        </p>

        <!-- video canvas & analytics -->
        <div class="monitor">
            <div class="video">
                <form method="post" class = 'upload-form' enctype="multipart/form-data" action = 'http://localhost:3333/getimg'>
                    <p class = 'description'>Загрузите изображение, чтобы проанализировать его</p>
                    <input type = 'file' name = 'img' class = 'CTA bg-orange' />
                    <button type = 'submit' name = 'submit' class = 'CTA bg-orange upload'>анализ</button>
                </form>
            </div>
            <Analytics { analytics } />
        </div>

        <!-- button: complete acceptance -->
        <button class="CTA complete-acceptance">завершить приемку</button>
    </div>

    <!-- [ section: process schedule ] -->
    <ProcessSchedule />

</main>
