<template>
<div>
  <div class="ui container">
    <div class="row">
      <div class="ui">
        <h1>Books</h1>
        <hr><br><br>
        <button type="button" class="ui button green" id="add">Add Book</button>
        <br><br>
        <table class="ui celled table">
          <thead>
            <tr>
              <th scope="col">Title</th>
              <th scope="col">Author</th>
              <th scope="col">Read</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(book, index) in books" :key="index">
              <td>{{ book.title }}</td>
              <td>{{ book.author }}</td>
              <td>
                <span v-if="book.read">Yes</span>
                <span v-else>No</span>
              </td>
              <td>
                <button type="button" class="ui button yellow">Update</button>
                <button type="button" class="ui button red">Delete</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
  <!-- start modal -->
  <div class="ui modal" id="book-modal" >
    <div class="header">
      Add a new book
    </div>
    <div class="content">
      <form class="ui form">
        <div class="field">
          <label>Title:</label>
          <input type="text" v-model="addBookForm.title"  placeholder="Game of Thrones">
        </div>
        <div class="field">
          <label>Author:</label>
          <input type="text" v-model="addBookForm.author" placeholder="George R. R. Martin">
        </div>
        <div class="field">
          <div class="ui checkbox">
            <input type="checkbox" value="true" id="form-checks" v-model="addBookForm.read">
            <label>Read</label>
          </div>
        </div>
        <div class="ui grid">
        <div class="four column row">
          <div class="right floated column">
            <div class="actions">
              <button type="reset" class="ui black deny button">Reset</button>
              <button type="submit" class="ui inverted green right button">Submit</button>
            </div>
          </div>
        </div>
        </div>
        
      </form>
    </div>

  </div>


</div>
</template>
<script>
import axios from 'axios';
//init semantic
$(function(){
  $("#add").click(function(){
    $('.modal').modal('show');
    });
    $(".modal").modal({
      closable: true
    });
})
//--------------------------------------------------------------------------------------------
export default {
  data() {
    return {
      books: [],
      addBookForm: {
        title: '',
        author: '',
        read: [],
      },
    };
  },
  methods: {
    getBooks() {
      const path = `http://localhost:5000/api/books`;
      axios.get(path)
        .then((res) => {
          this.books = res.data.books;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addBook(payload) {
      const path = `http://localhost:5000/api/books`;
      axios.post(path, payload)
        .then(() => {
          this.getBooks();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getBooks();
        });
    },
    initForm() {
      this.addBookForm.title = '';
      this.addBookForm.author = '';
      this.addBookForm.read = [];
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addBookModal.hide();
      let read = false;
      if (this.addBookForm.read[0]) read = true;
      const payload = {
        title: this.addBookForm.title,
        author: this.addBookForm.author,
        read, // property shorthand
      };
      this.addBook(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addBookModal.hide();
      this.initForm();
    },
  },
  created() {
    this.getBooks();
  },
};
</script>

