import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-template-sito',
  templateUrl: './template-sito.component.html',
  styleUrl: './template-sito.component.css'
})
export class TemplateSitoComponent implements OnInit{

  constructor(private apiService : ApiService){}

  ngOnInit(){
    this.apiService.getApi().subscribe(
      response =>{
        this.apiService = response;
      },
      error => {
        console.error(error)
      }
    )
  }

}
