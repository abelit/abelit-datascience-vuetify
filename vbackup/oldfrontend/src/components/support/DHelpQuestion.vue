<template>
  <v-tooltip bottom>
    <template v-slot:activator="{ on }">
      <v-btn icon v-on="on">
        <v-icon>contact_support</v-icon>
      </v-btn>
    </template>
    <span>{{$t("tooltip.QUESTION_SUPPORT")}}</span>
  </v-tooltip>
</template>
