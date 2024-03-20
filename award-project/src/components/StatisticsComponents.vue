<template>
    
<div class="surface-ground px-4 py-5 md:px-6 lg:px-8">
    <div class="grid">
        <div class="col-12 md:col-6 lg:col-3">
            <div class="surface-card shadow-2 p-3 border-round">
                <div class="flex justify-content-between mb-3">
                    <div>
                        <span class="block text-500 font-medium mb-3">Most successful member</span>
                        <div class="text-900 font-medium text-xl">{{ bestMember }}</div>
                    </div>
                   
                </div>
            </div>
        </div>
        <div class="col-12 md:col-6 lg:col-3">
            <div class="surface-card shadow-2 p-3 border-round">
                <div class="flex justify-content-between mb-3">
                    <div>
                        <span class="block text-500 font-medium mb-3">Most successful leader</span>
                        <div class="text-900 font-medium text-xl">{{ bestLeader }}</div>
                    </div>
                   
                </div>
               
            </div>
        </div>
        <div class="col-12 md:col-6 lg:col-3">
            <div class="surface-card shadow-2 p-3 border-round">
                <div class="flex justify-content-between mb-3">
                    <div>
                        <span class="block text-500 font-medium mb-3">Most successful team</span>
                        <div class="text-900 font-medium text-xl">{{ bestTeam }}</div>
                        
                    </div>
                    
                </div>
              
            </div>
        </div>
       
    </div>
</div>
</template>
<script setup lang="ts">
// @ts-ignore
import { getBestTeam, getBestLeader, getBestMember } from "@/utils/GetCalls.ts";
import { onMounted, ref } from "vue";

const bestTeam = ref("(loading...)");
const bestLeader = ref("(loading...)");
const bestMember = ref("(loading...)");

onMounted(() => {
    getBestTeam().then((res: any) => {
        return res.json();
    }).then((result: JSON) => {
        // @ts-ignore
        bestTeam.value = `Team ${result.team_id} with ${result.value} points`;
    });

    getBestLeader().then((res: any) => {
        return res.json();
    }).then((result: JSON) => {
        // @ts-ignore
        bestLeader.value = `${result.person_name} with ${result.sum_points} points (project count: ${result.project_count})`;
    });

    getBestMember().then((res: any) => {
        return res.json();
    }).then((result: JSON) => {
        // @ts-ignore
        bestMember.value = `${result.person_name} with ${result.sum_points} points (project count: ${result.project_count}, team count: ${result.team_count})`;
    });
});

</script>