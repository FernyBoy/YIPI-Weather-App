<template>
    <div class="question-box_container">
        <p class="question">¿De qué color es el sol?</p>
        <div class="answers-box">
            <p class="answer">Rojo</p>
            <p class="answer">Azul</p>
            <p class="answer">Blanco</p>
            <p class="answer">Amarillo</p>
        </div>
    </div>
</template>

<script setup lang="ts">

</script>

<style scoped lang="scss">
    .question-box_container
    {
        width: 100%;

        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        
        .question
        {
            margin-bottom: 35px;
            font-size: 2.3rem;
        }

        .answers-box
        {
            width: 100%;
            
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            
            .answer
            {
                width: 90%;
                margin-bottom: 15px;
                padding: 15px;
                
                border-radius: 50px;
                border: 2px solid white;

                font-size: 1.7rem;
            }
        }
    }
</style>