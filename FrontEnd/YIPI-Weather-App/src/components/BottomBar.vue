<template>
    <div class="bottom-bar_container">
        <div class="bottom-bar">
            <img class="bottom-bar_button" src="../assets/img/trivia-icon.png" alt="trivia-icon">
            <img class="bottom-bar_button" src="../assets/img/home-icon.png" alt="home-icon">
            <img id="profile-icon" class="bottom-bar_button" src="../assets/img/user-icon.png" alt="user-icon">
        </div>
    </div>
</template>

<script setup lang="ts">

</script>

<style scoped lang="scss">
    .bottom-bar_container
    {
        width: 100%;
        height: 100px;

        position: fixed;
        bottom: 20px;
        left: 50%;
        transform: translateX(-50%);
        
        display: flex;
        justify-content: center;
        align-items: center;

        .bottom-bar
        {
            width: 90%;
            height: 70%;

            display: flex;
            justify-content: space-evenly;
            align-items: center;

            border-radius: 50px;

            background-color: white;

            .bottom-bar_button
            {
                width: 50px;

                cursor: pointer;
            }

            #profile-icon
            {
                width: 40px;
            }
        }
    }
</style>