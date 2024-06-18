import { NgModule } from '@angular/core';
import { BrowserModule, provideClientHydration } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { TemplateSitoComponent } from './template-sito/template-sito.component';
import { HeaderComponent } from './header/header.component';
import { ModaleAccessoComponent } from './modale-accesso/modale-accesso.component';

@NgModule({
  declarations: [
    AppComponent,
    TemplateSitoComponent,
    HeaderComponent,
    ModaleAccessoComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [
    provideClientHydration()
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
