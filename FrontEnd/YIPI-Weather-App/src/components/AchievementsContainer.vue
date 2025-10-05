<template>
    <div class="achievements_container">
        <div class="achievements">
            <h1>Achievements</h1>
            <div class="medals">
                <figure class="circle"></figure>
                 <figure class="circle"></figure>
                 <figure class="circle"></figure>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">

</script>

<style scoped lang="scss">
    @import "../assets/styles/colors.scss";

    .achievements_container
    {
        width: 100%;
        height: 100px;

        position: fixed;
        top: 370px;
        left: 50%;
        transform: translateX(-50%);
        
        display: flex;
        
        justify-content: center;
        align-items: center;

        h1{
            font-size: 2.5rem;
        }

        .achievements
        {
            width: 90%;
            height: 140px;

            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;

            border-radius: 30px;
            margin: 10px;
            background-color: $golden;
            .medals{
                width: 70%;
                height: 70px;
                display: flex;
                align-items: center;
                justify-content:space-evenly;
                .circle{
                    width: 25px;
                    height: 25px;
                    background-color: goldenrod;
                    border-radius: 50%;
                }
            }
            

        }
    }
</style>