<template>
    <div class="Datas_container">
        <div class="first-line">
            <div class="UV-Ray">
                <p class="title-UV">UV Index</p>
                <p class="UV-total">4</p>
            </div>
            <div class="Wind">
                <p class="title-Wind">Wind</p>
                <p class="Wind-total">9.7 km/h</p>
            </div>
        </div>
        <div class="second-line">
            <div class="precipitation">
                <p class="title-Preci">Rainfall</p>
                <p class="Preci-total">1.8 mm</p>
            </div>
            <div class="windchill">
                <p class="title-WCh">Feels like</p>
                <p class="WCh-total">39</p>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">

</script>

<style scoped lang="scss">
    .Datas_container{
        width: 95%;
        height: 450px;
        top: 100px;
        border-radius: 50px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
       

        
        margin: 5px;
        .first-line{
            width: 100%;
            height: 50%;
            border-radius: 50px;
            display: flex;
            justify-content: center;
            align-items: center;
        
            margin: 10px;
            .UV-Ray{
                width: 50%;
                height: 210px;
                border-radius: 30px;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                background-color: blue;
                margin: 10px;
                border: 5px solid black;
                .title-UV{
                    font-size: 2.5rem;
                    margin: 20px;
                }
                .UV-total{
                   
                    font-size: 4rem;
                }
            }

            .Wind{
                width: 50%;
                height: 210px;
                border-radius: 30px;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                background-color: blue;
                margin: 10px;
                 border: 5px solid black;
                .title-Wind{
                    font-size: 2.5rem;
                    margin: 10px;
                }
                .Wind-total{
                    
                    font-size: 4rem;
                }
            }

        }
        .second-line{
            width: 100%;
            height:50%;
            border-radius: 50px;
            display: flex;
            justify-content: center;
            align-items: center;
           
            margin: 10px;
             .precipitation{
                width: 50%;
                height: 210px;
                border-radius: 30px;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                background-color: blue;
                margin: 10px;
                 border: 5px solid black;
                .title-Preci{
                    font-size: 2.5rem;
                    margin: 10px;
                }
                .Preci-total{
                   
                    font-size: 4rem;
                }
            }

            .windchill{
                width: 50%;
                height: 210px;
                border-radius: 30px;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                background-color: blue;
                margin: 10px;
                 border: 5px solid black;
                .title-WCh{
                    font-size: 2.5rem;
                    margin: 20px;
                }
                .WCh-total{
                   
                    font-size: 4rem;
                }
            }
            

        }
    }
</style>