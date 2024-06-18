import { Component } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrl: './header.component.css'
})
export class HeaderComponent {

  constructor(private apiService : ApiService){}

  loginButton() {
    //this.apiService.getApi().subscribe(
      //response =>{
        //this.apiService = response;
      //},
      //error => {
        //console.error(error)
      //}
    //)
    console.log("Accesso")
  }
  registerButton() {
    
  }

}
