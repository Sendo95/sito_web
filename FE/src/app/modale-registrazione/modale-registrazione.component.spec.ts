import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ModaleRegistrazioneComponent } from './modale-registrazione.component';

describe('ModaleRegistrazioneComponent', () => {
  let component: ModaleRegistrazioneComponent;
  let fixture: ComponentFixture<ModaleRegistrazioneComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ModaleRegistrazioneComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ModaleRegistrazioneComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
