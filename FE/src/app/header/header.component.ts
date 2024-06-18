import { Component, OnInit} from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrl: './header.component.css'
})
export class HeaderComponent implements OnInit{

  constructor(private apiService : ApiService){}

  ngOnInit(){

  }

  loginButton(){
    this.apiService.getApi().subscribe(
      response =>{
        this.apiService = response;
        console.log(response);
      },
      error => {
        console.error(error)
      }
    )
  }
  registerButton(){

  }
}