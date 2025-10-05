<template>
    <div class="streak-box_container">
        <img src="../assets/img/yip/streak-yip.png" alt="">
        <div class="streak-box">
            <h1>4 Days</h1>
            <div class="streak-points_container">
                <div class="streak-point">
                    <p class="streak-point_day">Mo</p>
                    <figure class="streak-point_circle"></figure>
                </div>
                <div class="streak-point">
                    <p class="streak-point_day">Tu</p>
                    <figure class="streak-point_circle"></figure>
                </div>
                <div class="streak-point">
                    <p class="streak-point_day">We</p>
                    <figure class="streak-point_circle"></figure>
                </div>
                <div class="streak-point">
                    <p class="streak-point_day">Th</p>
                    <figure class="streak-point_circle"></figure>
                </div>
                <div class="streak-point">
                    <p class="streak-point_day">Fr</p>
                    <figure class="streak-point_circle"></figure>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">

</script>

<style scoped lang="scss">
    @import '../assets/styles/colors.scss';

    .streak-box_container
    {
        width: 100%;
        height: 100%;

        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;

        img
        {
            width: 20%;
        }

        .streak-box
        {
            width: 85%;
            height: 85%;
            padding: 30px;

            border-radius: 30px;
            border: 10px solid rgb(255, 123, 0);

            display: flex;
            flex-direction: column;
            justify-content: space-between;
            align-content: center;

            h1
            {
                font-size: 6rem;
            }

            .streak-points_container
            {
                width: 100%;

                display: flex;
                justify-content: space-around;

                .streak-point
                {
                    display: flex;
                    flex-direction: column;

                    .streak-point_day
                    {
                        margin-bottom: 15px;
                        font-size: 2.5rem;
                    }

                    .streak-point_circle
                    {
                        width: 35px;
                        height: 35px;

                        border-radius: 50%;

                        background-color: $streak-blue;
                    }
                }
            }

            img
            {
                width: 40px;

                justify-self: flex-end;
                align-self: flex-end;
            }
        }
    }
</style>