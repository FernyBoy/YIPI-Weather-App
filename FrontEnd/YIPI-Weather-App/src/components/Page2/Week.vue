<template>
    <div class="Week">
        <div class="day">
            <p class="name-day"> Mon </p>
            <img id="partycloudy-icon" class="partycloudy" src="../../assets/img/part-cloudy-icon.png" alt="partcloudy-icon">
            <p class="temperature"> 36 </p>
            <p class="precipitation"> 2 mm</p>
        </div>
        <div class="day">
            <p class="name-day"> Tue </p>
            <img id="partycloudy-icon" class="partycloudy" src="../../assets/img/part-cloudy-icon.png" alt="partcloudy-icon">
            <p class="temperature"> 36 </p>
            <p class="precipitation"> 2 mm</p>
        </div>
        <div class="day">
            <p class="name-day"> Wed </p>
            <img id="partycloudy-icon" class="partycloudy" src="../../assets/img/part-cloudy-icon.png" alt="partcloudy-icon">
            <p class="temperature"> 36 </p>
            <p class="precipitation"> 2 mm</p>
        </div>
        <div class="day">
            <p class="name-day"> Thu </p>
            <img id="partycloudy-icon" class="partycloudy" src="../../assets/img/part-cloudy-icon.png" alt="partcloudy-icon">
            <p class="temperature"> 36 </p>
            <p class="precipitation"> 2 mm</p>
        </div>
        <div class="day">
            <p class="name-day"> Fri </p>
            <img id="partycloudy-icon" class="partycloudy" src="../../assets/img/part-cloudy-icon.png" alt="partcloudy-icon">
            <p class="temperature"> 36 </p>
            <p class="precipitation"> 2 mm</p>
        </div>
        <div class="day">
            <p class="name-day">Sat</p>
            <img id="partycloudy-icon" class="partycloudy" src="../../assets/img/part-cloudy-icon.png" alt="partcloudy-icon">
            <p class="temperature"> 36 </p>
            <p class="precipitation"> 2 mm</p>
        </div>
    </div>
</template>

<script setup lang="ts">

</script>

<style scoped lang="scss">
    .Week{
        width: 95%;
        height: 350px;
        top: 100px;
        border-radius: 50px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        background-color: white;
        margin: 10px;
         border: 5px solid blue;
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

</style>