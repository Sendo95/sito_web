import { NgModule } from '@angular/core';
import { BrowserModule, provideClientHydration } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { TemplateSitoComponent } from './template-sito/template-sito.component';
import { HeaderComponent } from './header/header.component';
import { ApiService } from './api.service';
import { HttpClientModule } from '@angular/common/http';
import { ModaleAccessoComponent } from './modale-accesso/modale-accesso.component';
import { FormsModule } from '@angular/forms';
import { provideAnimationsAsync } from '@angular/platform-browser/animations/async';
import { MatDialogModule } from '@angular/material/dialog';
import { MatInputModule } from '@angular/material/input';
import { MatIconModule } from '@angular/material/icon';
import { ModaleRegistrazioneComponent } from './modale-registrazione/modale-registrazione.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';


@NgModule({
  declarations: [
    AppComponent,
    TemplateSitoComponent,
    HeaderComponent,
    ModaleAccessoComponent,
    ModaleRegistrazioneComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    MatDialogModule,
    MatInputModule,
    MatIconModule,
    BrowserAnimationsModule
  ],
  providers: [
    provideClientHydration(), ApiService, provideAnimationsAsync()
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
