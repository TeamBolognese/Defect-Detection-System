
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
    let extra_analytics_requested  = false;
    let analytics_received         = false;
    let acceptance_complete        = false;
    let uploaded_img  = 'https://final.teambolognese.ru/res.png';
    const analytics = {
        status:      'good',      // has defects / no defects
        percent:     0,          // percentage
        invoice:     0,    // price of no-defect cargo
    }


    // [ HOOKS ]
    onMount(() => {
        
        // get > image analytics from URI
        const urlParams = new URLSearchParams(window.location.search);
        let status = urlParams.get('status');
        let percent = urlParams.get('percent');
        
        if( status !== null && percent !== null) {
            analytics.status  = status
            analytics.percent = percent
            console.log(analytics.percent);
            analytics.invoice = 2100205
            analytics_received = true
            uploaded_img = uploaded_img
        }

        renderCanvas(analytics.percent);

        
    });


</script>


<!-- [ TEMPLATE: Monitoring ] -->
<svelte:head>
    <title>Monitoring</title>
</svelte:head>

<!-- modal: image analytics -->
{#if extra_analytics_requested}
    <div class="modal-result">
        <div class="overlay" on:click={ () => { analytics_received = false } }></div>
        <div class="message">
            <h5 class="title">Результаты анализа:</h5>
            <div class="content">
                <p>{ 'status  = ' + analytics.status  }</p>
                <p>{ 'percent = ' + analytics.percent }</p>
            </div>
        </div>
    </div>
{/if}

<main in:fade='{{ duration: 100 }}' out:fade|local='{{ duration: 100 }}' class = 'monitoring'>

    <!-- [ section: zone tabs ] -->
    <ul class = 'zone-tabs'>
        <li class="tab"><a href = '/'>Зона А</a></li>
        <li class="tab active"><a href = 'zoneB'>Зона Б</a></li>
        <li class="tab"><a href = 'zoneC'>Зона В</a></li>
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
            <div class="video { analytics_received ? 'uploaded' : '' }">
                {#if analytics_received}
                    <img src="{ uploaded_img }" class = 'uploaded-img' alt="uploaded img">
                {/if}
                <form method="post" class = 'upload-form' enctype="multipart/form-data" action = 'http://localhost:3333/upload'>
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
