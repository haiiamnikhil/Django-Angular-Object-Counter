import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ObjectcountComponent } from './objectcount.component';

describe('ObjectcountComponent', () => {
  let component: ObjectcountComponent;
  let fixture: ComponentFixture<ObjectcountComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ObjectcountComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ObjectcountComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
