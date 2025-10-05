<template>
    <div class="stats_container">
        <div class="stats">
            <div class="stats_row">
                <div class="stats_box">
                    <p class="box_title">UV Index</p>
                    <p class="box_data">4</p>
                </div>
                <div class="stats_box">
                    <p class="box_title">Wind</p>
                    <p class="box_data">9.7 km/h</p>
                </div>
            </div>
            <div class="stats_row">
                <div class="stats_box">
                    <p class="box_title">Rainfall</p>
                    <p class="box_data">1.8 mm</p>
                </div>
                <div class="stats_box">
                    <p class="box_title">Feels like</p>
                    <p class="box_data">39</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">

</script>

<style scoped lang="scss">
@import '../../assets/styles/colors.scss';

    .stats_container
    {
        width: 100%;

        display: flex;
        justify-content: center;

        
        .stats
        {
            width: 90%;
            aspect-ratio: 1 / 1;
            padding-bottom: 120px;

            display: flex;
            flex-direction: column;
            justify-content: space-between;
            align-content: space-between;

            .stats_row
            {
                width: 100%;

                display: flex;
                justify-content: space-between;
                align-items: center;

                .stats_box
                {
                    width: 47%;
                    aspect-ratio: 1 / 1;

                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;

                    border-radius: 30px;
                    border: 5px solid $dark-blue;

                    background-color: $light-blue;

                    .box_title
                    {
                        margin-bottom: 15px;
                        font-size: 2rem;
                    }

                    .box_data
                    {
                        font-size: 1.7rem;
                    }
                }
            }
        }
    }
</style>