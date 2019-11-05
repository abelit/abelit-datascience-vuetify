<template>
  <div class="text-center">
    <v-menu offset-y>
      <template v-slot:activator="{ on: menu }">
          <v-tooltip bottom>
            <template v-slot:activator="{ on: tooltip }">
              <v-btn color="transparent" v-on="{ ...tooltip, ...menu}" icon dark>
                <v-avatar size="32px" tile>
                <v-img :src="require('@/assets/images/lang/'+language+'.png')" aspect-ratio="1" alt="language"></v-img>
                </v-avatar>
              </v-btn>
            </template>
            <!-- <span>{{ $t("tooltip.langSwitch") }}</span> -->
          </v-tooltip>
      </template>
      <v-list>
        <v-list-item
          v-for="(lang, index) in langList"
          :key="index"
          :disabled="language === lang.code"
        >
          <v-list-item-avatar>
            <v-avatar size="32px" tile @click="setLanguage(lang.code)">
              <v-img :src="require('@/assets/images/lang/'+lang.code+'.png')" alt="language" > </v-img>
            </v-avatar>
          </v-list-item-avatar>
          <v-list-item-title @click="setLanguage(lang.code)">{{ lang.name }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
  </div>
</template>


<script>
export default {
  data: () => ({
    language: "zh_CN",
    langList: [
      {
        code: "zh_CN",
        name: "简体中文"
      },
      {
        code: "en_US",
        name: "English"
      }
    ]
  }),
  methods: {
    // 语言切换
    setLanguage(lang) {
      this.language = lang;
      // 设置国际化语言信息
      this.$i18n.locale = lang;
      // 设置验证语言信息
      this.$validator.locale = lang;

      // 通过异步方式调用store中setLanguage方法，保存语言信息
      this.$store.dispatch("setLanguage", lang);
    }
  },
  mounted() {
    // 从vuex中获取语言信息
    // this.language = this.$store.state.language;
  }
};
</script>