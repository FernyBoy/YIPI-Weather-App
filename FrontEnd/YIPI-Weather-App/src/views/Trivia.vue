<template>
    <div class="trivia_container">
        <BottomBar />
        <div class="trivia">
            <StreakBox id="streak-box_module"/>
            <QuestionBox id="question-box_module"/>
        </div>
    </div>
</template>

<script setup lang="ts">
import BottomBar from '@/components/BottomBar.vue';
import StreakBox from '@/components/StreakBox.vue';
import QuestionBox from '@/components/QuestionBox.vue';
</script>

<style scoped lang="scss">
    .trivia_container
    {
        width: 100%;
        height: 100%;

        .trivia
        {
            width: 100%;
            height: 100%;
    
            #streak-box_module
            {
                height: 40%;
                padding-top: 30px;
            }
    
            #question-box_module
            {
                height: 50%;
            }
        }
    }
</style>