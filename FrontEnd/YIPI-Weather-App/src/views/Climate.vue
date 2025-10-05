<template>
    <div class="climate_container">
        <BottomBar />
        <div class="climate">
            <Week />
            <Datas_container />
        </div>
    </div>
</template>

<script setup lang="ts">
    import BottomBar from '@/components/BottomBar.vue';
    import Week from '@/components/Page2/Week.vue';
    import Datas_container from '@/components/Page2/Datas.vue'
</script>


<style scoped lang="scss">

    .climate_container
    {
        width: 100%;
        height: 100%;

        .climate
        {
            width: 100%;
            display: flex;
            flex-direction:column;
            justify-content: center;
            align-content: center;
        }


    }
</style>