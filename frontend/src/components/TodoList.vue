<template>
  <section>
    <div class=hero-body>
      <div class="container">
        <div class="column is-6 is-offset-3">
          <div class="box has-text-left">
            <div
              v-for="todo in todos"
              :key="todo.id">
              <b-checkbox
                :id="todo.id"
                :value="todo.is_done"
                :checked="todo.is_done">
                {{ todo.content }}
              </b-checkbox>
            </div>
          </div>
          <div class="field has-text-right">
            <button class="button is-primary" @click="actionGetTodos">
              Get Todos
            </button>
            <button class="button is-danger" @click="actionClearTodos">
              Clear Todos
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  computed: {
    ...mapGetters({
      todos: 'todos',
      error: 'error',
    }),
  },
  methods: {
    ...mapActions([
      'actionGetTodos',
      'actionClearTodos',
    ]),
  },
  mounted() {
    this.actionGetTodos();
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
