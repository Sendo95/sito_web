import { Component, OnInit } from '@angular/core';
import { ApiServiceService } from '../api-service.service';
import { response } from 'express';

@Component({
  selector: 'app-template-sito',
  standalone: true,
  imports: [],
  templateUrl: './template-sito.component.html',
  styleUrl: './template-sito.component.css'
})
export class TemplateSitoComponent implements OnInit{

  constructor(private apiService : ApiServiceService){}

  ngOnInit() {
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
