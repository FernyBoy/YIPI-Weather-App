<template>
    <div class="week_container">
        <div class="week">
            <div class="day">
                <p class="name-day"> Mon </p>
                <img id="partycloudy-icon" class="partycloudy" src="../../assets/img/part-cloudy-icon.png" alt="partcloudy-icon">
                <p class="temperature"> 32 </p>
                <p class="precipitation"> 8 mm</p>
            </div>
            <div class="day">
                <p class="name-day"> Tue </p>
                <img id="partycloudy-icon" class="partycloudy" src="../../assets/img/part-cloudy-icon.png" alt="partcloudy-icon">
                <p class="temperature"> 30 </p>
                <p class="precipitation"> 6 mm</p>
            </div>
            <div class="day">
                <p class="name-day"> Wed </p>
                <img id="partycloudy-icon" class="partycloudy" src="../../assets/img/part-cloudy-icon.png" alt="partcloudy-icon">
                <p class="temperature"> 32 </p>
                <p class="precipitation"> 4 mm</p>
            </div>
            <div class="day">
                <p class="name-day"> Thu </p>
                <img id="partycloudy-icon" class="partycloudy" src="../../assets/img/part-cloudy-icon.png" alt="partcloudy-icon">
                <p class="temperature"> 37 </p>
                <p class="precipitation"> 5 mm</p>
            </div>
            <div class="day">
                <p class="name-day"> Fri </p>
                <img id="partycloudy-icon" class="partycloudy" src="../../assets/img/part-cloudy-icon.png" alt="partcloudy-icon">
                <p class="temperature"> 30 </p>
                <p class="precipitation"> 1 mm</p>
            </div>
            <div class="day">
                <p class="name-day">Sat</p>
                <img id="partycloudy-icon" class="partycloudy" src="../../assets/img/part-cloudy-icon.png" alt="partcloudy-icon">
                <p class="temperature"> 35 </p>
                <p class="precipitation"> 2 mm</p>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">

</script>

<style scoped lang="scss">
@import '../../assets/styles/colors.scss';

    .week_container
    {
        width: 100%;
        
        display: flex;
        justify-content: center;
        align-items: center;

        .week
        {
            width: 90%;
            height: 350px;
            top: 100px;
            border-radius: 40px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            background-color: white;
            margin: 10px;
            border: 5px solid $dark-blue;
            
            .day{
                width: 95%;
                height: 50px;
                
                display: flex;
                justify-content: space-evenly;
                align-items: center;
                
                .name-day{
                    width: 20%;
                    color: black;
                    font-size: 2.5rem;
                }
                
                #partycloudy-icon{
                    
                    width: 10%;
                }
                
                .temperature{
                    width: 25%;
                    color: black;
                    font-size: 2.5rem;
                }
                
                .precipitation{
                    width: 25%;
                    color: black;
                    font-size: 2.5rem;
                }
            }   
        }
    }

</style>