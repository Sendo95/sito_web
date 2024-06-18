import { Component } from '@angular/core';

@Component({
  selector: 'app-template-sito',
  templateUrl: './template-sito.component.html',
  styleUrl: './template-sito.component.css'
})
export class TemplateSitoComponent {

  constructor() { }

  onClick() {
    console.log('cliccato')
  }

}
