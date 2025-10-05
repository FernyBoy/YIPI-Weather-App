<template>
    <div class="trivia_container">
        <BottomBar />
        <div class="trivia">
            <div class="trivia_title">
                <h1 class="trivia_name">Trivia</h1>
                <p class="trivia_date">10/26/25</p>
            </div>
            <div class="trivia_question">
                <p>ON A SUMMER DAY, WHEN MIGHT YOU BE AT THE HIGHEST RISK FOR A UV SUNBURN?</p>
                <img src="../assets/img/yip/yip.png" alt="">
            </div>
            <div class="trivia_answers">
                <div class="answer_container">
                    <div class="answer_index">
                        <p>A</p>
                    </div>
                    <p class="answer_text">Only on a perfectly clear, cloudless day.</p>
                </div>
                <div class="answer_container">
                    <div class="answer_index">
                        <p>B</p>
                    </div>
                    <p class="answer_text">On a partly cloudy day.</p>
                </div>
                <div class="answer_container">
                    <div class="answer_index">
                        <p>C</p>
                    </div>
                    <p class="answer_text">Only when the temperature is above 35°C.</p>
                </div>
                <div class="answer_container">
                    <div class="answer_index">
                        <p>D</p>
                    </div>
                    <p class="answer_text">During the first hour after sunrise.</p>
                </div>
            </div>

            <StreakBox id="streak-box_module"/>
        </div>
    </div>
</template>

<script setup lang="ts">
import BottomBar from '@/components/BottomBar.vue';
import StreakBox from '@/components/StreakBox.vue';
import QuestionBox from '@/components/QuestionBox.vue';
</script>

<style scoped lang="scss">
@import '../assets/styles/colors.scss';

    .trivia_container
    {
        width: 100%;
        height: 100%;

        .trivia
        {
            width: 100%;
            height: 100%;
            
            display: flex;
            flex-direction: column;
            align-items: center;

            .trivia_title
            {
                width: 100%;
                margin-top: 30px;
                margin-bottom: 30px;

                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;

                .trivia_name
                {
                    font-size: 3.5rem;
                }

                .trivia_date
                {
                    font-size: 2rem;
                }
            }

            .trivia_question
            {
                width: 90%;

                display: flex;
                justify-content: center;
                align-items: center;

                p 
                {
                    width: 50%;
                    padding: 20px;

                    border-radius: 30px;

                    background-color: $light-blue;

                    font-size: 2rem;
                }

                img 
                {
                    width: 30%;
                    margin: 20px;
                }
            }

            .trivia_answers
            {
                width: 90%;

                display: flex;
                flex-direction: column;

                .answer_container
                {
                    width: 100%;
                    margin-top: 20px;

                    display: flex;
                    justify-content: space-between;

                    .answer_index
                    {
                        width: 30px;
                        height: 30px;
                        
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        
                        border-radius: 50%;

                        background-color: white;
                       
                        p
                        {                                 
                            font-size: 1.5rem;
                            color: $dark-blue;
                            
                        }
                    }

                    .answer_text
                    {
                        width: 90%;
                        padding: 20px;

                        border-radius: 30px;

                        color: $dark-blue;
                        font-size: 2.3rem;

                        background-color: white;
                    }
                }
            }
    
            #streak-box_module
            {
                margin-top: 120px;
                padding-bottom: 120px;
            }
        }
    }
</style>