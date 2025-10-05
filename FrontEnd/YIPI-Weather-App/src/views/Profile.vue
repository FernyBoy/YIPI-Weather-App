<template>
    <div class="profile_container">
        <BottomBar />
        <div class="profile">
            <ProfilePhoto />
            <AchievementsContainer />
        </div>
    </div>
</template>

<script setup lang="ts">
    import AchievementsContainer from '@/components/AchievementsContainer.vue';
    import BottomBar from '@/components/BottomBar.vue';
    import ProfilePhoto from '@/components/ProfilePhoto.vue';
</script>

<style scoped lang="scss">
    .profile_container
    {
        width: 100%;
        height: 100%;
 
        .profile
        {
            width: 100%;
            display: flex;
            flex-direction:column;
            justify-content: center;
            align-content: center;
        }

    }
    
</style>