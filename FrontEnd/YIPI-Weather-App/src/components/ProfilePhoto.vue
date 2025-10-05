<template>
    <div class="profile-photo_container">
        <div class="profile-photo">
            <img id="profile-icon" class="bottom-bar_button" src="../assets/img/user-icon.png" alt="user-icon">
        </div>
        <h1>Hi, buddy</h1>
    </div>
</template>

<script setup lang="ts">

</script>

<style scoped lang="scss">
.profile-photo_container
    {
        width: 50%;
        height: 150px;

        position: fixed;
        top: 120px;
        
        left: 50%;
        transform: translateX(-50%);
        
        display: flex;
        flex-direction:column;
        justify-content: center;
        align-items: center;
        
        .profile-photo{
            width: 100%;
            height: 100%;
            border-radius: 50px;
            margin: 35px;

            background-color: white;
            
            display: flex;
            
            justify-content: center;
            align-items: center;
            #profile-icon
            {
                width: 140px;
            }
        }

        h1{
            font-size: 4rem;
        }
    }
</style>