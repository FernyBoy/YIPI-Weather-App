<template>
    <div class="climate_container">
        <BottomBar /> 

        <div class="Search-Bar_container">
            <div class="Search-Bar">
                <input class="Search-Bar_text" type="text" placeholder="Search">
                <img class="Search-Bar_icon" src="../assets/img/search-icon.png">
            </div>
        </div>
        <div class="climate-location_container">
            <div class="climate-location">
                <p class="climate-location_city">Hermosillo</p>
                <p class="climate-location_day">Monday</p>    
            </div>
        </div>
        <div class="climate-figures_container">
            <div class="climate-figures">
                <img class="climate-figures_yip" src="../assets/img/yip/sunny.png" alt="Sunny Yip">
                <div class="climate-figures_info">
                    <img class="climate-figures_icon" src="../assets/img/climates/sunny.png" alt="">
                    <div class="climate-figures_temperature">
                        <p>35</p>
                        <p>°C</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import BottomBar from '../components/BottomBar.vue';
</script>

<style scoped lang="scss">
    .Search-Bar_container
    {
        width: 100%;
        height: 100px;

        display: flex;
        justify-content: center;
        align-items: center;

        .Search-Bar
        {
            width: 90%;
            height: 50px;

            display: flex;
            justify-content: space-between;
            align-items: center;

            border-radius: 50px;

            background-color: white;

            .Search-Bar_text
            {
                width: 80%;
                height: 90%;
                margin-left: 30px;

                border: 0;

                font-family: Monocraft;
                font-size: 2rem;
                color: #5f5f5f;

                &:focus
                {
                    border: 0px;
                    outline: none;
                }
            }

            .Search-Bar_icon
            {
                width: 35px;
                margin-right: 20px;
                opacity: 0.6;
            }
        }

    }
    
    .climate-location_container
    {
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;

        .climate-location
        {
            width: 90%;

            .climate-location_city
            {
                font-size: 3rem;
            }

            .climate-location_day
            {
                margin-top: 5px;
                font-size: 2rem;
            }
        }
    }

    .climate-figures_container
    {
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;

        .climate-figures
        {
            width: 90%;

            display: flex;
            justify-content: center;
            align-items: center;

            .climate-figures_yip
            {
                width: 60%;
            }
    
            .climate-figures_info
            {
                width: 40%;

                display: flex;
                flex-direction: column;
                justify-content: space-evenly;
                align-items: center;

                .climate-figures_icon
                {
                    width: 60%;
                }
                
                .climate-figures_temperature
                {
                    width: 50%;
                    
                    display: flex;
                    flex-direction: column;
                    align-items: center;

                    p
                    {
                        font-size: 4.5rem;
                    }
                }
            }
        }

    }
</style>