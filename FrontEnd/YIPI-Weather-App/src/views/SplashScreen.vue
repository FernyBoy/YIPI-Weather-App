<template>
    <div class="splash-screen_contaier">
        <div class="splash-screen">
            <img class="splash-screen_img Rotating-Object" src="../assets/img/yip/loading-icon.png" alt="">
        </div>
    </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

onMounted(() => {
    setTimeout(() => {
        router.push('/climate') // <-- cambia la ruta a donde quieres ir
    }, 3000) // 3 segundos
})
</script>

<style scoped lang="scss">
    .splash-screen_contaier
    {
        width: 100%;
        height: 100vh;
        
        .splash-screen
        {            
            width: 100%;
            height: 100vh;

            display: flex;
            justify-content: center;
            align-items: center;
            
            .splash-screen_img
            {
                width: 200px;
            }
        }
    }

    @keyframes rotate360 
    {
        from {
            transform: rotate(0deg);
        }
        to {
            transform: rotate(360deg);
        }
    }

    .Rotating-Object 
    {
        animation: rotate360 2s linear infinite; // velocidad + tipo + bucle infinito
    }
</style>