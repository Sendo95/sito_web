import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ModaleAccessoComponent } from './modale-accesso.component';

describe('ModaleAccessoComponent', () => {
  let component: ModaleAccessoComponent;
  let fixture: ComponentFixture<ModaleAccessoComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ModaleAccessoComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ModaleAccessoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
