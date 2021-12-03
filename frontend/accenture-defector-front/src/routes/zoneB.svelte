
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
        defects:     false,      // has defects / no defects
        defect_rate: 0,          // percentage
        invoice:     2100205,    // price of no-defect cargo
    }


    //@ upload > img
    let img;

    async function uploadImg(){

        const dataArray = new FormData();
        dataArray.append("uploadFile", img);

        let res = await fetch("https://accenture-final.teambolognese.ru/upload", {
            mode: 'cors',
            method: "POST",
            headers: {
                "Access-Control-Allow-Origin": "*",
                "Content-Type": "multipart/form-data",
            },
            body: dataArray
        })

        console.log(res.body)
    } 


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
        <li class="tab"><a href = '/'>Зона А</a></li>
        <li class="tab active"><a href = 'zoneB'>Зона Б</a></li>
        <li class="tab">Зона В</li>
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
                <form on:submit={ uploadImg }>
                    <input type = 'file' bind:files={ img } class = 'CTA bg-orange' />
                    <a on:click={ uploadImg } class = 'CTA bg-orange upload'>upload</a>
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
