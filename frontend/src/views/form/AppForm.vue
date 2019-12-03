<template>
  <v-container fluid>
    <v-row>
      <v-col cols="8" md="8">
        <vuedraggable :list="list" class="list-group">
          <v-text-field v-for="(item,index) in list" v-model="formData[item.model]" :key="index" :label="item.label" outlined clearable></v-text-field>
        </vuedraggable>
        <v-btn @click="save">Save</v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>